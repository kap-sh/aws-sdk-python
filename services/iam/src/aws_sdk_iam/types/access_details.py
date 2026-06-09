"""Generated from Smithy shape ``com.amazonaws.iam#AccessDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.access_detail

AccessDetails: TypeAlias = list["aws_sdk_iam.types.access_detail.AccessDetail"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.access_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.access_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AccessDetails:
    import aws_sdk_iam.types.access_detail

    out: AccessDetails = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.access_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AccessDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.access_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.access_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AccessDetails:
    import aws_sdk_iam.types.access_detail

    out: AccessDetails = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.access_detail.deserialize_query(child))
    return out
