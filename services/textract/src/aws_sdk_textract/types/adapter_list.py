"""Generated from Smithy shape ``com.amazonaws.textract#AdapterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_overview

AdapterList: TypeAlias = list["aws_sdk_textract.types.adapter_overview.AdapterOverview"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterList) -> list:
    import aws_sdk_textract.types.adapter_overview

    out: list = []
    for item in value:
        out.append(aws_sdk_textract.types.adapter_overview.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AdapterList:
    import aws_sdk_textract.types.adapter_overview

    out: AdapterList = []
    for item in data:
        out.append(
            aws_sdk_textract.types.adapter_overview.deserialize_aws_json_1_1(item)
        )
    return out
