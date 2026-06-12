"""Generated from Smithy shape ``com.amazonaws.mpa#GetIdentitySourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.identity_source_parameters_for_get
    import aws_sdk_mpa.types.identity_source_status
    import aws_sdk_mpa.types.identity_source_status_code
    import aws_sdk_mpa.types.identity_source_type
    import aws_sdk_mpa.types.iso_timestamp
    import aws_sdk_mpa.types.string


class GetIdentitySourceResponse(TypedDict):
    identity_source_type: NotRequired[
        "aws_sdk_mpa.types.identity_source_type.IdentitySourceType"
    ]
    """<p>The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    identity_source_parameters: NotRequired[
        "aws_sdk_mpa.types.identity_source_parameters_for_get.IdentitySourceParametersForGet"
    ]
    """<p>A <code> IdentitySourceParameters</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    identity_source_arn: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the identity source.</p>"""
    creation_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the identity source was created.</p>"""
    status: NotRequired["aws_sdk_mpa.types.identity_source_status.IdentitySourceStatus"]
    """<p>Status for the identity source. For example, if the identity source is <code>ACTIVE</code>.</p>"""
    status_code: NotRequired[
        "aws_sdk_mpa.types.identity_source_status_code.IdentitySourceStatusCode"
    ]
    """<p>Status code of the identity source.</p>"""
    status_message: NotRequired["aws_sdk_mpa.types.string.String"]
    """<p>Message describing the status for the identity source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentitySourceResponse) -> dict:
    out: dict = {}
    if "identity_source_type" in value:
        import aws_sdk_mpa.types.identity_source_type

        out["IdentitySourceType"] = (
            aws_sdk_mpa.types.identity_source_type.serialize_json(
                value["identity_source_type"]
            )
        )
    if "identity_source_parameters" in value:
        import aws_sdk_mpa.types.identity_source_parameters_for_get

        out["IdentitySourceParameters"] = (
            aws_sdk_mpa.types.identity_source_parameters_for_get.serialize_json(
                value["identity_source_parameters"]
            )
        )
    if "identity_source_arn" in value:
        out["IdentitySourceArn"] = value["identity_source_arn"]
    if "creation_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["CreationTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        import aws_sdk_mpa.types.identity_source_status

        out["Status"] = aws_sdk_mpa.types.identity_source_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import aws_sdk_mpa.types.identity_source_status_code

        out["StatusCode"] = (
            aws_sdk_mpa.types.identity_source_status_code.serialize_json(
                value["status_code"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> GetIdentitySourceResponse:
    out: GetIdentitySourceResponse = {}  # type: ignore[typeddict-item]
    if "IdentitySourceType" in data:
        import aws_sdk_mpa.types.identity_source_type

        out["identity_source_type"] = (
            aws_sdk_mpa.types.identity_source_type.deserialize_json(
                data["IdentitySourceType"]
            )
        )
    if "IdentitySourceParameters" in data:
        import aws_sdk_mpa.types.identity_source_parameters_for_get

        out["identity_source_parameters"] = (
            aws_sdk_mpa.types.identity_source_parameters_for_get.deserialize_json(
                data["IdentitySourceParameters"]
            )
        )
    if "IdentitySourceArn" in data:
        out["identity_source_arn"] = data["IdentitySourceArn"]
    if "CreationTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["creation_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "Status" in data:
        import aws_sdk_mpa.types.identity_source_status

        out["status"] = aws_sdk_mpa.types.identity_source_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import aws_sdk_mpa.types.identity_source_status_code

        out["status_code"] = (
            aws_sdk_mpa.types.identity_source_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
