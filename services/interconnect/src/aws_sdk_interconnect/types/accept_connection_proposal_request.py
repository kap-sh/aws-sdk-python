"""Generated from Smithy shape ``com.amazonaws.interconnect#AcceptConnectionProposalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.activation_key
    import aws_sdk_interconnect.types.attach_point
    import aws_sdk_interconnect.types.connection_description
    import aws_sdk_interconnect.types.tag_map


class AcceptConnectionProposalRequest(TypedDict, closed=True):
    attach_point: "aws_sdk_interconnect.types.attach_point.AttachPoint"
    """<p>The Attach Point to which the connection should be associated.</p>"""
    activation_key: "aws_sdk_interconnect.types.activation_key.ActivationKey"
    """<p>An Activation Key that was generated on a supported partner's portal. This key captures the desired parameters from the initial creation request.</p> <p>The details of this request can be described using with <a>DescribeConnectionProposal</a>. </p>"""
    description: NotRequired[
        "aws_sdk_interconnect.types.connection_description.ConnectionDescription"
    ]
    """<p>A description to distinguish this <a>Connection</a>.</p>"""
    tags: NotRequired["aws_sdk_interconnect.types.tag_map.TagMap"]
    """<p>The tags to associate with the resulting <a>Connection</a>.</p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptConnectionProposalRequest) -> dict:
    out: dict = {}
    import aws_sdk_interconnect.types.attach_point

    out["attachPoint"] = aws_sdk_interconnect.types.attach_point.serialize_aws_json_1_0(
        value["attach_point"]
    )
    out["activationKey"] = value["activation_key"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptConnectionProposalRequest:
    out: AcceptConnectionProposalRequest = {}  # type: ignore[typeddict-item]
    if "attachPoint" in data:
        import aws_sdk_interconnect.types.attach_point

        out["attach_point"] = (
            aws_sdk_interconnect.types.attach_point.deserialize_aws_json_1_0(
                data["attachPoint"]
            )
        )
    else:
        raise DeserializationError(
            "AcceptConnectionProposalRequest.attach_point required"
        )
    if "activationKey" in data:
        out["activation_key"] = data["activationKey"]
    else:
        raise DeserializationError(
            "AcceptConnectionProposalRequest.activation_key required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_interconnect.types.tag_map

        out["tags"] = aws_sdk_interconnect.types.tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
