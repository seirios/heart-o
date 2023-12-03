LUDB_PATH := ../../datasets/physionet.org/files/ludb/1.0.1/data

all-ludb:
	seq 1 200 \
		| parallel $(MAKE) ludb/{}.csv

ludb/%.csv: | ludb/
	python ludb_to_csv.py $(LUDB_PATH) $* $@

%/:
	mkdir -p $@
