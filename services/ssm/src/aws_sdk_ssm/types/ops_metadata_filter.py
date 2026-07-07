"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadataFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_metadata_filter_key
    import aws_sdk_ssm.types.ops_metadata_filter_value_list


class OpsMetadataFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.ops_metadata_filter_key.OpsMetadataFilterKey"
    """<p>A filter key.</p>"""
    values: (
        "aws_sdk_ssm.types.ops_metadata_filter_value_list.OpsMetadataFilterValueList"
    )
    """<p>A filter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadataFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_ssm.types.ops_metadata_filter_value_list

    out["Values"] = (
        aws_sdk_ssm.types.ops_metadata_filter_value_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadataFilter:
    out: OpsMetadataFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("OpsMetadataFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.ops_metadata_filter_value_list

        out["values"] = (
            aws_sdk_ssm.types.ops_metadata_filter_value_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("OpsMetadataFilter.values required")
    return out
