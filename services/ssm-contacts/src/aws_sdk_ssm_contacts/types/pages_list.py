"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#PagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.page

PagesList: TypeAlias = list["aws_sdk_ssm_contacts.types.page.Page"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PagesList) -> list:
    import aws_sdk_ssm_contacts.types.page

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.page.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PagesList:
    import aws_sdk_ssm_contacts.types.page

    out: PagesList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.page.deserialize_aws_json_1_1(item))
    return out
