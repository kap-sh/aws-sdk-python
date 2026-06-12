"""Generated from Smithy shape ``com.amazonaws.mpa#CreateIdentitySourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.identity_source_type
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.string


class CreateIdentitySourceResponse(TypedDict):
    identity_source_type: NotRequired[
        "aws_sdk_mpa.types.identity_source_type.IdentitySourceType"
    ]
    """<p>The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    identity_source_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the identity source that was created.</p>"""
    creation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the identity source was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdentitySourceResponse) -> dict:
    out: dict = {}
    if "identity_source_type" in value:
        import aws_sdk_mpa.types.identity_source_type

        out["IdentitySourceType"] = (
            aws_sdk_mpa.types.identity_source_type.serialize_json(
                value["identity_source_type"]
            )
        )
    if "identity_source_arn" in value:
        out["IdentitySourceArn"] = value["identity_source_arn"]
    if "creation_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["CreationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateIdentitySourceResponse:
    out: CreateIdentitySourceResponse = {}  # type: ignore[typeddict-item]
    if "IdentitySourceType" in data:
        import aws_sdk_mpa.types.identity_source_type

        out["identity_source_type"] = (
            aws_sdk_mpa.types.identity_source_type.deserialize_json(
                data["IdentitySourceType"]
            )
        )
    if "IdentitySourceArn" in data:
        out["identity_source_arn"] = data["IdentitySourceArn"]
    if "CreationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["creation_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
