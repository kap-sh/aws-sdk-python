"""Generated from Smithy shape ``com.amazonaws.redshift#AquaConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

AquaConfigurationStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "auto",
]


# --- awsQuery ser/de ---
def to_query_text(value: AquaConfigurationStatus) -> str:
    return value


def from_query_text(text: str) -> AquaConfigurationStatus:
    return cast(AquaConfigurationStatus, text)


def serialize_query(
    value: AquaConfigurationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AquaConfigurationStatus:
    return from_query_text(el.text or "")
