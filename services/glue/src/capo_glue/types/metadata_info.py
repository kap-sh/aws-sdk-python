"""Generated from Smithy shape ``com.amazonaws.glue#MetadataInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.created_timestamp
    import capo_glue.types.metadata_value_string
    import capo_glue.types.other_metadata_value_list


class MetadataInfo(TypedDict, closed=True):
    metadata_value: NotRequired[
        "capo_glue.types.metadata_value_string.MetadataValueString"
    ]
    """<p>The metadata key’s corresponding value.</p>"""
    created_time: NotRequired["capo_glue.types.created_timestamp.CreatedTimestamp"]
    """<p>The time at which the entry was created.</p>"""
    other_metadata_value_list: NotRequired[
        "capo_glue.types.other_metadata_value_list.OtherMetadataValueList"
    ]
    """<p>Other metadata belonging to the same metadata key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataInfo) -> dict:
    out: dict = {}
    if "metadata_value" in value:
        out["MetadataValue"] = value["metadata_value"]
    if "created_time" in value:
        out["CreatedTime"] = value["created_time"]
    if "other_metadata_value_list" in value:
        import capo_glue.types.other_metadata_value_list

        out["OtherMetadataValueList"] = (
            capo_glue.types.other_metadata_value_list.serialize_aws_json_1_1(
                value["other_metadata_value_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataInfo:
    out: MetadataInfo = {}  # type: ignore[typeddict-item]
    if "MetadataValue" in data:
        out["metadata_value"] = data["MetadataValue"]
    if "CreatedTime" in data:
        out["created_time"] = data["CreatedTime"]
    if "OtherMetadataValueList" in data:
        import capo_glue.types.other_metadata_value_list

        out["other_metadata_value_list"] = (
            capo_glue.types.other_metadata_value_list.deserialize_aws_json_1_1(
                data["OtherMetadataValueList"]
            )
        )
    return out
