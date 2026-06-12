"""Generated from Smithy shape ``com.amazonaws.emrcontainers#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.in_transit_encryption_configuration


class EncryptionConfiguration(TypedDict):
    in_transit_encryption_configuration: NotRequired[
        "aws_sdk_emr_containers.types.in_transit_encryption_configuration.InTransitEncryptionConfiguration"
    ]
    """<p>In-transit encryption-related input for the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "in_transit_encryption_configuration" in value:
        import aws_sdk_emr_containers.types.in_transit_encryption_configuration

        out["inTransitEncryptionConfiguration"] = (
            aws_sdk_emr_containers.types.in_transit_encryption_configuration.serialize_json(
                value["in_transit_encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "inTransitEncryptionConfiguration" in data:
        import aws_sdk_emr_containers.types.in_transit_encryption_configuration

        out["in_transit_encryption_configuration"] = (
            aws_sdk_emr_containers.types.in_transit_encryption_configuration.deserialize_json(
                data["inTransitEncryptionConfiguration"]
            )
        )
    return out
