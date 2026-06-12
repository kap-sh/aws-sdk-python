"""Generated from Smithy shape ``com.amazonaws.opensearch#VolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The type of EBS volume that a domain uses. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-createupdatedomains.html#opensearch-createdomain-configure-ebs\">Configuring EBS-based storage</a>.</p>"""
VolumeType: TypeAlias = Literal[
    "standard",
    "gp2",
    "io1",
    "gp3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "gp2",
        "io1",
        "gp3",
    )
)


def serialize_json(value: VolumeType) -> str:
    return value


def deserialize_json(data: str) -> VolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeType value: {data!r}")
    return cast(VolumeType, data)
