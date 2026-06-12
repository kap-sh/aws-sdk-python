"""Generated from Smithy shape ``com.amazonaws.cloudformation#RequiredActivatedTypes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.required_activated_type

RequiredActivatedTypes: TypeAlias = list[
    "aws_sdk_cloudformation.types.required_activated_type.RequiredActivatedType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RequiredActivatedTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.required_activated_type

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.required_activated_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> RequiredActivatedTypes:
    import aws_sdk_cloudformation.types.required_activated_type

    out: RequiredActivatedTypes = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.required_activated_type.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: RequiredActivatedTypes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.required_activated_type

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.required_activated_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RequiredActivatedTypes:
    import aws_sdk_cloudformation.types.required_activated_type

    out: RequiredActivatedTypes = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.required_activated_type.deserialize_query(
                child
            )
        )
    return out
