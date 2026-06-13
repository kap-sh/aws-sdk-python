"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#KeyspacesCellValue``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_keyspacesstreams.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_list
    import aws_sdk_keyspacesstreams.types.keyspaces_cell_map
    import aws_sdk_keyspacesstreams.types.keyspaces_udt_map


class _KeyspacesCellValue_asciiT(TypedDict):
    asciiT: "str"


class _KeyspacesCellValue_bigintT(TypedDict):
    bigintT: "str"


class _KeyspacesCellValue_blobT(TypedDict):
    blobT: "bytes"


class _KeyspacesCellValue_boolT(TypedDict):
    boolT: "bool"


class _KeyspacesCellValue_counterT(TypedDict):
    counterT: "str"


class _KeyspacesCellValue_dateT(TypedDict):
    dateT: "str"


class _KeyspacesCellValue_decimalT(TypedDict):
    decimalT: "str"


class _KeyspacesCellValue_doubleT(TypedDict):
    doubleT: "str"


class _KeyspacesCellValue_durationT(TypedDict):
    durationT: "str"


class _KeyspacesCellValue_floatT(TypedDict):
    floatT: "str"


class _KeyspacesCellValue_inetT(TypedDict):
    inetT: "str"


class _KeyspacesCellValue_intT(TypedDict):
    intT: "str"


class _KeyspacesCellValue_listT(TypedDict):
    listT: "aws_sdk_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class _KeyspacesCellValue_mapT(TypedDict):
    mapT: "aws_sdk_keyspacesstreams.types.keyspaces_cell_map.KeyspacesCellMap"


class _KeyspacesCellValue_setT(TypedDict):
    setT: "aws_sdk_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class _KeyspacesCellValue_smallintT(TypedDict):
    smallintT: "str"


class _KeyspacesCellValue_textT(TypedDict):
    textT: "str"


class _KeyspacesCellValue_timeT(TypedDict):
    timeT: "str"


class _KeyspacesCellValue_timestampT(TypedDict):
    timestampT: "str"


class _KeyspacesCellValue_timeuuidT(TypedDict):
    timeuuidT: "str"


class _KeyspacesCellValue_tinyintT(TypedDict):
    tinyintT: "str"


class _KeyspacesCellValue_tupleT(TypedDict):
    tupleT: "aws_sdk_keyspacesstreams.types.keyspaces_cell_list.KeyspacesCellList"


class _KeyspacesCellValue_uuidT(TypedDict):
    uuidT: "str"


class _KeyspacesCellValue_varcharT(TypedDict):
    varcharT: "str"


class _KeyspacesCellValue_varintT(TypedDict):
    varintT: "str"


class _KeyspacesCellValue_udtT(TypedDict):
    udtT: "aws_sdk_keyspacesstreams.types.keyspaces_udt_map.KeyspacesUdtMap"


KeyspacesCellValue: TypeAlias = (
    _KeyspacesCellValue_asciiT
    | _KeyspacesCellValue_bigintT
    | _KeyspacesCellValue_blobT
    | _KeyspacesCellValue_boolT
    | _KeyspacesCellValue_counterT
    | _KeyspacesCellValue_dateT
    | _KeyspacesCellValue_decimalT
    | _KeyspacesCellValue_doubleT
    | _KeyspacesCellValue_durationT
    | _KeyspacesCellValue_floatT
    | _KeyspacesCellValue_inetT
    | _KeyspacesCellValue_intT
    | _KeyspacesCellValue_listT
    | _KeyspacesCellValue_mapT
    | _KeyspacesCellValue_setT
    | _KeyspacesCellValue_smallintT
    | _KeyspacesCellValue_textT
    | _KeyspacesCellValue_timeT
    | _KeyspacesCellValue_timestampT
    | _KeyspacesCellValue_timeuuidT
    | _KeyspacesCellValue_tinyintT
    | _KeyspacesCellValue_tupleT
    | _KeyspacesCellValue_uuidT
    | _KeyspacesCellValue_varcharT
    | _KeyspacesCellValue_varintT
    | _KeyspacesCellValue_udtT
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyspacesCellValue) -> dict:
    if "asciiT" in value:
        return {"asciiT": value["asciiT"]}
    elif "bigintT" in value:
        return {"bigintT": value["bigintT"]}
    elif "blobT" in value:
        import aws_sdk_keyspacesstreams.types._prelude.blob

        return {
            "blobT": aws_sdk_keyspacesstreams.types._prelude.blob.serialize_aws_json_1_0(
                value["blobT"]
            )
        }
    elif "boolT" in value:
        return {"boolT": value["boolT"]}
    elif "counterT" in value:
        return {"counterT": value["counterT"]}
    elif "dateT" in value:
        return {"dateT": value["dateT"]}
    elif "decimalT" in value:
        return {"decimalT": value["decimalT"]}
    elif "doubleT" in value:
        return {"doubleT": value["doubleT"]}
    elif "durationT" in value:
        return {"durationT": value["durationT"]}
    elif "floatT" in value:
        return {"floatT": value["floatT"]}
    elif "inetT" in value:
        return {"inetT": value["inetT"]}
    elif "intT" in value:
        return {"intT": value["intT"]}
    elif "listT" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "listT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["listT"]
            )
        }
    elif "mapT" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_map

        return {
            "mapT": aws_sdk_keyspacesstreams.types.keyspaces_cell_map.serialize_aws_json_1_0(
                value["mapT"]
            )
        }
    elif "setT" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "setT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["setT"]
            )
        }
    elif "smallintT" in value:
        return {"smallintT": value["smallintT"]}
    elif "textT" in value:
        return {"textT": value["textT"]}
    elif "timeT" in value:
        return {"timeT": value["timeT"]}
    elif "timestampT" in value:
        return {"timestampT": value["timestampT"]}
    elif "timeuuidT" in value:
        return {"timeuuidT": value["timeuuidT"]}
    elif "tinyintT" in value:
        return {"tinyintT": value["tinyintT"]}
    elif "tupleT" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "tupleT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.serialize_aws_json_1_0(
                value["tupleT"]
            )
        }
    elif "uuidT" in value:
        return {"uuidT": value["uuidT"]}
    elif "varcharT" in value:
        return {"varcharT": value["varcharT"]}
    elif "varintT" in value:
        return {"varintT": value["varintT"]}
    elif "udtT" in value:
        import aws_sdk_keyspacesstreams.types.keyspaces_udt_map

        return {
            "udtT": aws_sdk_keyspacesstreams.types.keyspaces_udt_map.serialize_aws_json_1_0(
                value["udtT"]
            )
        }
    else:
        raise SerializationError("KeyspacesCellValue: no variant present")


def deserialize_aws_json_1_0(data: dict) -> KeyspacesCellValue:
    if "asciiT" in data:
        return {"asciiT": data["asciiT"]}
    elif "bigintT" in data:
        return {"bigintT": data["bigintT"]}
    elif "blobT" in data:
        import aws_sdk_keyspacesstreams.types._prelude.blob

        return {
            "blobT": aws_sdk_keyspacesstreams.types._prelude.blob.deserialize_aws_json_1_0(
                data["blobT"]
            )
        }
    elif "boolT" in data:
        return {"boolT": data["boolT"]}
    elif "counterT" in data:
        return {"counterT": data["counterT"]}
    elif "dateT" in data:
        return {"dateT": data["dateT"]}
    elif "decimalT" in data:
        return {"decimalT": data["decimalT"]}
    elif "doubleT" in data:
        return {"doubleT": data["doubleT"]}
    elif "durationT" in data:
        return {"durationT": data["durationT"]}
    elif "floatT" in data:
        return {"floatT": data["floatT"]}
    elif "inetT" in data:
        return {"inetT": data["inetT"]}
    elif "intT" in data:
        return {"intT": data["intT"]}
    elif "listT" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "listT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["listT"]
            )
        }
    elif "mapT" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_map

        return {
            "mapT": aws_sdk_keyspacesstreams.types.keyspaces_cell_map.deserialize_aws_json_1_0(
                data["mapT"]
            )
        }
    elif "setT" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "setT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["setT"]
            )
        }
    elif "smallintT" in data:
        return {"smallintT": data["smallintT"]}
    elif "textT" in data:
        return {"textT": data["textT"]}
    elif "timeT" in data:
        return {"timeT": data["timeT"]}
    elif "timestampT" in data:
        return {"timestampT": data["timestampT"]}
    elif "timeuuidT" in data:
        return {"timeuuidT": data["timeuuidT"]}
    elif "tinyintT" in data:
        return {"tinyintT": data["tinyintT"]}
    elif "tupleT" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_cell_list

        return {
            "tupleT": aws_sdk_keyspacesstreams.types.keyspaces_cell_list.deserialize_aws_json_1_0(
                data["tupleT"]
            )
        }
    elif "uuidT" in data:
        return {"uuidT": data["uuidT"]}
    elif "varcharT" in data:
        return {"varcharT": data["varcharT"]}
    elif "varintT" in data:
        return {"varintT": data["varintT"]}
    elif "udtT" in data:
        import aws_sdk_keyspacesstreams.types.keyspaces_udt_map

        return {
            "udtT": aws_sdk_keyspacesstreams.types.keyspaces_udt_map.deserialize_aws_json_1_0(
                data["udtT"]
            )
        }
    else:
        raise DeserializationError("KeyspacesCellValue: no recognized variant key")
