"""Generated from Smithy shape ``com.amazonaws.firehose#Deserializer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.hive_json_ser_de
    import aws_sdk_firehose.types.open_x_json_ser_de


class Deserializer(TypedDict, closed=True):
    open_x_json_ser_de: NotRequired[
        "aws_sdk_firehose.types.open_x_json_ser_de.OpenXJsonSerDe"
    ]
    """<p>The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.</p>"""
    hive_json_ser_de: NotRequired[
        "aws_sdk_firehose.types.hive_json_ser_de.HiveJsonSerDe"
    ]
    """<p>The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Deserializer) -> dict:
    out: dict = {}
    if "open_x_json_ser_de" in value:
        import aws_sdk_firehose.types.open_x_json_ser_de

        out["OpenXJsonSerDe"] = (
            aws_sdk_firehose.types.open_x_json_ser_de.serialize_aws_json_1_1(
                value["open_x_json_ser_de"]
            )
        )
    if "hive_json_ser_de" in value:
        import aws_sdk_firehose.types.hive_json_ser_de

        out["HiveJsonSerDe"] = (
            aws_sdk_firehose.types.hive_json_ser_de.serialize_aws_json_1_1(
                value["hive_json_ser_de"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Deserializer:
    out: Deserializer = {}  # type: ignore[typeddict-item]
    if "OpenXJsonSerDe" in data:
        import aws_sdk_firehose.types.open_x_json_ser_de

        out["open_x_json_ser_de"] = (
            aws_sdk_firehose.types.open_x_json_ser_de.deserialize_aws_json_1_1(
                data["OpenXJsonSerDe"]
            )
        )
    if "HiveJsonSerDe" in data:
        import aws_sdk_firehose.types.hive_json_ser_de

        out["hive_json_ser_de"] = (
            aws_sdk_firehose.types.hive_json_ser_de.deserialize_aws_json_1_1(
                data["HiveJsonSerDe"]
            )
        )
    return out
