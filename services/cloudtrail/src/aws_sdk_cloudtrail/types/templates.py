"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Templates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.template

Templates: TypeAlias = list["aws_sdk_cloudtrail.types.template.Template"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Templates) -> list:
    import aws_sdk_cloudtrail.types.template

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudtrail.types.template.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Templates:
    import aws_sdk_cloudtrail.types.template

    out: Templates = []
    for item in data:
        out.append(aws_sdk_cloudtrail.types.template.deserialize_aws_json_1_1(item))
    return out
