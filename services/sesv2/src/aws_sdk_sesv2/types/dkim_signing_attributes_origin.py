"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimSigningAttributesOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

DkimSigningAttributesOrigin: TypeAlias = Literal[
    "AWS_SES",
    "EXTERNAL",
    "AWS_SES_AF_SOUTH_1",
    "AWS_SES_EU_NORTH_1",
    "AWS_SES_AP_SOUTH_1",
    "AWS_SES_EU_WEST_3",
    "AWS_SES_EU_WEST_2",
    "AWS_SES_EU_SOUTH_1",
    "AWS_SES_EU_WEST_1",
    "AWS_SES_AP_NORTHEAST_3",
    "AWS_SES_AP_NORTHEAST_2",
    "AWS_SES_ME_SOUTH_1",
    "AWS_SES_AP_NORTHEAST_1",
    "AWS_SES_IL_CENTRAL_1",
    "AWS_SES_SA_EAST_1",
    "AWS_SES_CA_CENTRAL_1",
    "AWS_SES_AP_SOUTHEAST_1",
    "AWS_SES_AP_SOUTHEAST_2",
    "AWS_SES_AP_SOUTHEAST_3",
    "AWS_SES_EU_CENTRAL_1",
    "AWS_SES_US_EAST_1",
    "AWS_SES_US_EAST_2",
    "AWS_SES_US_WEST_1",
    "AWS_SES_US_WEST_2",
    "AWS_SES_ME_CENTRAL_1",
    "AWS_SES_AP_SOUTH_2",
    "AWS_SES_EU_CENTRAL_2",
    "AWS_SES_AP_SOUTHEAST_5",
    "AWS_SES_CA_WEST_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_SES",
        "EXTERNAL",
        "AWS_SES_AF_SOUTH_1",
        "AWS_SES_EU_NORTH_1",
        "AWS_SES_AP_SOUTH_1",
        "AWS_SES_EU_WEST_3",
        "AWS_SES_EU_WEST_2",
        "AWS_SES_EU_SOUTH_1",
        "AWS_SES_EU_WEST_1",
        "AWS_SES_AP_NORTHEAST_3",
        "AWS_SES_AP_NORTHEAST_2",
        "AWS_SES_ME_SOUTH_1",
        "AWS_SES_AP_NORTHEAST_1",
        "AWS_SES_IL_CENTRAL_1",
        "AWS_SES_SA_EAST_1",
        "AWS_SES_CA_CENTRAL_1",
        "AWS_SES_AP_SOUTHEAST_1",
        "AWS_SES_AP_SOUTHEAST_2",
        "AWS_SES_AP_SOUTHEAST_3",
        "AWS_SES_EU_CENTRAL_1",
        "AWS_SES_US_EAST_1",
        "AWS_SES_US_EAST_2",
        "AWS_SES_US_WEST_1",
        "AWS_SES_US_WEST_2",
        "AWS_SES_ME_CENTRAL_1",
        "AWS_SES_AP_SOUTH_2",
        "AWS_SES_EU_CENTRAL_2",
        "AWS_SES_AP_SOUTHEAST_5",
        "AWS_SES_CA_WEST_1",
    )
)


def serialize_json(value: DkimSigningAttributesOrigin) -> str:
    return value


def deserialize_json(data: str) -> DkimSigningAttributesOrigin:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DkimSigningAttributesOrigin value: {data!r}"
        )
    return cast(DkimSigningAttributesOrigin, data)
