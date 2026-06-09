"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReferenceResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ImageReferenceResourceType: TypeAlias = Literal[
    "ec2:Instance",
    "ec2:LaunchTemplate",
    "ssm:Parameter",
    "imagebuilder:ImageRecipe",
    "imagebuilder:ContainerRecipe",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ec2:Instance",
        "ec2:LaunchTemplate",
        "ssm:Parameter",
        "imagebuilder:ImageRecipe",
        "imagebuilder:ContainerRecipe",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "ec2:Instance",
        "ec2:LaunchTemplate",
        "ssm:Parameter",
        "imagebuilder:ImageRecipe",
        "imagebuilder:ContainerRecipe",
    )
)


def to_ec2_query_text(value: ImageReferenceResourceType) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageReferenceResourceType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ImageReferenceResourceType value: {text!r}"
        )
    return cast(ImageReferenceResourceType, text)


def serialize_ec2_query(
    value: ImageReferenceResourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageReferenceResourceType:
    return from_ec2_query_text(el.text or "")
