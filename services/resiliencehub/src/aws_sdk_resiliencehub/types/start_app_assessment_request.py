"""Generated from Smithy shape ``com.amazonaws.resiliencehub#StartAppAssessmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.client_token
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.entity_version
    import aws_sdk_resiliencehub.types.tag_map


class StartAppAssessmentRequest(TypedDict):
    app_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "aws_sdk_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    assessment_name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>The name for the assessment.</p>"""
    client_token: NotRequired["aws_sdk_resiliencehub.types.client_token.ClientToken"]
    """<p>Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAppAssessmentRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    out["assessmentName"] = value["assessment_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartAppAssessmentRequest:
    out: StartAppAssessmentRequest = {}  # type: ignore[typeddict-item]
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("StartAppAssessmentRequest.app_arn required")
    if "appVersion" in data:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("StartAppAssessmentRequest.app_version required")
    if "assessmentName" in data:
        out["assessment_name"] = data["assessmentName"]
    else:
        raise DeserializationError("StartAppAssessmentRequest.assessment_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    return out
