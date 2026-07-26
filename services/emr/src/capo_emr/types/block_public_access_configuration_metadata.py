"""Generated from Smithy shape ``com.amazonaws.emr#BlockPublicAccessConfigurationMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.arn_type
    import capo_emr.types.date


class BlockPublicAccessConfigurationMetadata(TypedDict, closed=True):
    creation_date_time: NotRequired["capo_emr.types.date.Date"]
    """<p>The date and time that the configuration was created.</p>"""
    created_by_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name that created or last modified the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockPublicAccessConfigurationMetadata) -> dict:
    out: dict = {}
    if "creation_date_time" in value:
        import capo_emr.types.date

        out["CreationDateTime"] = capo_emr.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "created_by_arn" in value:
        out["CreatedByArn"] = value["created_by_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockPublicAccessConfigurationMetadata:
    out: BlockPublicAccessConfigurationMetadata = {}  # type: ignore[typeddict-item]
    if "CreationDateTime" in data:
        import capo_emr.types.date

        out["creation_date_time"] = capo_emr.types.date.deserialize_aws_json_1_1(
            data["CreationDateTime"]
        )
    if "CreatedByArn" in data:
        out["created_by_arn"] = data["CreatedByArn"]
    return out
