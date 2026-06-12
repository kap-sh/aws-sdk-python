"""Generated from Smithy shape ``com.amazonaws.sns#SMSSandboxPhoneNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.sms_sandbox_phone_number

SMSSandboxPhoneNumberList: TypeAlias = list[
    "aws_sdk_sns.types.sms_sandbox_phone_number.SMSSandboxPhoneNumber"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SMSSandboxPhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.sms_sandbox_phone_number

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.sms_sandbox_phone_number.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SMSSandboxPhoneNumberList:
    import aws_sdk_sns.types.sms_sandbox_phone_number

    out: SMSSandboxPhoneNumberList = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.sms_sandbox_phone_number.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SMSSandboxPhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.sms_sandbox_phone_number

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.sms_sandbox_phone_number.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SMSSandboxPhoneNumberList:
    import aws_sdk_sns.types.sms_sandbox_phone_number

    out: SMSSandboxPhoneNumberList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.sms_sandbox_phone_number.deserialize_query(child))
    return out
