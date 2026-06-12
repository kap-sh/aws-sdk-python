"""Generated from Smithy shape ``com.amazonaws.redshift#AuthenticationProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.authentication_profile

AuthenticationProfileList: TypeAlias = list[
    "aws_sdk_redshift.types.authentication_profile.AuthenticationProfile"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthenticationProfileList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.authentication_profile

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.authentication_profile.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AuthenticationProfileList:
    import aws_sdk_redshift.types.authentication_profile

    out: AuthenticationProfileList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_redshift.types.authentication_profile.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AuthenticationProfileList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.authentication_profile

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.authentication_profile.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AuthenticationProfileList:
    import aws_sdk_redshift.types.authentication_profile

    out: AuthenticationProfileList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.authentication_profile.deserialize_query(child)
        )
    return out
