"""Generated from Smithy shape ``com.amazonaws.emr#StartSessionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.arn_type
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.session_id
    import aws_sdk_emr.types.session_state
    import aws_sdk_emr.types.xml_string_max_len256


class StartSessionOutput(TypedDict):
    id: NotRequired["aws_sdk_emr.types.session_id.SessionId"]
    """<p>The output contains the ID of the session.</p>"""
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster that the session was started on.</p>"""
    arn: NotRequired["aws_sdk_emr.types.arn_type.ArnType"]
    """<p>The output contains the ARN of the session.</p>"""
    account_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon Web Services account ID that owns the session.</p>"""
    state: NotRequired["aws_sdk_emr.types.session_state.SessionState"]
    """<p>The state of the session at the time the request returned. When a session is first created, it enters the <code>SUBMITTED</code> state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "state" in value:
        import aws_sdk_emr.types.session_state

        out["State"] = aws_sdk_emr.types.session_state.serialize_aws_json_1_1(
            value["state"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionOutput:
    out: StartSessionOutput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "State" in data:
        import aws_sdk_emr.types.session_state

        out["state"] = aws_sdk_emr.types.session_state.deserialize_aws_json_1_1(
            data["State"]
        )
    return out
