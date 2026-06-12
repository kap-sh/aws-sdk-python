"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.account_limit

AccountLimitList: TypeAlias = list[
    "aws_sdk_cloudformation.types.account_limit.AccountLimit"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccountLimitList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.account_limit

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.account_limit.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AccountLimitList:
    import aws_sdk_cloudformation.types.account_limit

    out: AccountLimitList = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.account_limit.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccountLimitList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.account_limit

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.account_limit.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AccountLimitList:
    import aws_sdk_cloudformation.types.account_limit

    out: AccountLimitList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.account_limit.deserialize_query(child))
    return out
