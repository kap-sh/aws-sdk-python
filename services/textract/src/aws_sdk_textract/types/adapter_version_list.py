"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_version_overview

AdapterVersionList: TypeAlias = list[
    "aws_sdk_textract.types.adapter_version_overview.AdapterVersionOverview"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionList) -> list:
    import aws_sdk_textract.types.adapter_version_overview

    out: list = []
    for item in value:
        out.append(
            aws_sdk_textract.types.adapter_version_overview.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdapterVersionList:
    import aws_sdk_textract.types.adapter_version_overview

    out: AdapterVersionList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.adapter_version_overview.deserialize_aws_json_1_1(
                item
            )
        )
    return out
