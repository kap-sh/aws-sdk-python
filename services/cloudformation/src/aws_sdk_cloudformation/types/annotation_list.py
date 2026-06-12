"""Generated from Smithy shape ``com.amazonaws.cloudformation#AnnotationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.annotation

AnnotationList: TypeAlias = list["aws_sdk_cloudformation.types.annotation.Annotation"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AnnotationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.annotation

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.annotation.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AnnotationList:
    import aws_sdk_cloudformation.types.annotation

    out: AnnotationList = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.annotation.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AnnotationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.annotation

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.annotation.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AnnotationList:
    import aws_sdk_cloudformation.types.annotation

    out: AnnotationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.annotation.deserialize_query(child))
    return out
