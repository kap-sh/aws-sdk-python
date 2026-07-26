"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceForList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.identity_source_parameters_for_list
    import capo_mpa.types.identity_source_status
    import capo_mpa.types.identity_source_status_code
    import capo_mpa.types.identity_source_type
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.string


class IdentitySourceForList(TypedDict, closed=True):
    identity_source_type: NotRequired[
        "capo_mpa.types.identity_source_type.IdentitySourceType"
    ]
    """<p>The type of resource that provided identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    identity_source_parameters: NotRequired[
        "capo_mpa.types.identity_source_parameters_for_list.IdentitySourceParametersForList"
    ]
    """<p>A <code>IdentitySourceParametersForList</code> object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.</p>"""
    identity_source_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the identity source.</p>"""
    creation_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the identity source was created.</p>"""
    status: NotRequired["capo_mpa.types.identity_source_status.IdentitySourceStatus"]
    """<p>Status for the identity source. For example, if the identity source is <code>ACTIVE</code>.</p>"""
    status_code: NotRequired[
        "capo_mpa.types.identity_source_status_code.IdentitySourceStatusCode"
    ]
    """<p>Status code of the identity source.</p>"""
    status_message: NotRequired["capo_mpa.types.string.String"]
    """<p>Message describing the status for the identity source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceForList) -> dict:
    out: dict = {}
    if "identity_source_type" in value:
        import capo_mpa.types.identity_source_type

        out["IdentitySourceType"] = capo_mpa.types.identity_source_type.serialize_json(
            value["identity_source_type"]
        )
    if "identity_source_parameters" in value:
        import capo_mpa.types.identity_source_parameters_for_list

        out["IdentitySourceParameters"] = (
            capo_mpa.types.identity_source_parameters_for_list.serialize_json(
                value["identity_source_parameters"]
            )
        )
    if "identity_source_arn" in value:
        out["IdentitySourceArn"] = value["identity_source_arn"]
    if "creation_time" in value:
        import capo_mpa.types.iso_timestamp

        out["CreationTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "status" in value:
        import capo_mpa.types.identity_source_status

        out["Status"] = capo_mpa.types.identity_source_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import capo_mpa.types.identity_source_status_code

        out["StatusCode"] = capo_mpa.types.identity_source_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> IdentitySourceForList:
    out: IdentitySourceForList = {}  # type: ignore[typeddict-item]
    if "IdentitySourceType" in data:
        import capo_mpa.types.identity_source_type

        out["identity_source_type"] = (
            capo_mpa.types.identity_source_type.deserialize_json(
                data["IdentitySourceType"]
            )
        )
    if "IdentitySourceParameters" in data:
        import capo_mpa.types.identity_source_parameters_for_list

        out["identity_source_parameters"] = (
            capo_mpa.types.identity_source_parameters_for_list.deserialize_json(
                data["IdentitySourceParameters"]
            )
        )
    if "IdentitySourceArn" in data:
        out["identity_source_arn"] = data["IdentitySourceArn"]
    if "CreationTime" in data:
        import capo_mpa.types.iso_timestamp

        out["creation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "Status" in data:
        import capo_mpa.types.identity_source_status

        out["status"] = capo_mpa.types.identity_source_status.deserialize_json(
            data["Status"]
        )
    if "StatusCode" in data:
        import capo_mpa.types.identity_source_status_code

        out["status_code"] = (
            capo_mpa.types.identity_source_status_code.deserialize_json(
                data["StatusCode"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
