"""Generated from Smithy shape ``com.amazonaws.ec2#ImageBlockPublicAccessEnabledState``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

ImageBlockPublicAccessEnabledState: TypeAlias = Literal["block-new-sharing",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("block-new-sharing",))


_VALUES: frozenset[str] = frozenset(("block-new-sharing",))


def to_ec2_query_text(value: ImageBlockPublicAccessEnabledState) -> str:
    return value


def from_ec2_query_text(text: str) -> ImageBlockPublicAccessEnabledState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ImageBlockPublicAccessEnabledState value: {text!r}"
        )
    return cast(ImageBlockPublicAccessEnabledState, text)


def serialize_ec2_query(
    value: ImageBlockPublicAccessEnabledState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ImageBlockPublicAccessEnabledState:
    return from_ec2_query_text(el.text or "")
