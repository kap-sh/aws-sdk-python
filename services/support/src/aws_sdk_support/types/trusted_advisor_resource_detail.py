"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorResourceDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.boolean
    import aws_sdk_support.types.string
    import aws_sdk_support.types.string_list


class TrustedAdvisorResourceDetail(TypedDict):
    status: "aws_sdk_support.types.string.String"
    """<p>The status code for the resource identified in the Trusted Advisor check.</p>"""
    region: NotRequired["aws_sdk_support.types.string.String"]
    """<p>The Amazon Web Services Region in which the identified resource is located.</p>"""
    resource_id: "aws_sdk_support.types.string.String"
    """<p>The unique identifier for the identified resource.</p>"""
    is_suppressed: "aws_sdk_support.types.boolean.Boolean"
    """<p>Specifies whether the Amazon Web Services resource was ignored by Trusted Advisor because it was marked as suppressed by the user.</p>"""
    metadata: "aws_sdk_support.types.string_list.StringList"
    """<p>Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the <a>TrustedAdvisorCheckDescription</a> object returned by the call to <a>DescribeTrustedAdvisorChecks</a>. <b>Metadata</b> contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorResourceDetail) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "region" in value:
        out["region"] = value["region"]
    out["resourceId"] = value["resource_id"]
    out["isSuppressed"] = value.get("is_suppressed", False)
    import aws_sdk_support.types.string_list

    out["metadata"] = aws_sdk_support.types.string_list.serialize_aws_json_1_1(
        value["metadata"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorResourceDetail:
    out: TrustedAdvisorResourceDetail = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("TrustedAdvisorResourceDetail.status required")
    if "region" in data:
        out["region"] = data["region"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("TrustedAdvisorResourceDetail.resource_id required")
    if "isSuppressed" in data:
        out["is_suppressed"] = data["isSuppressed"]
    else:
        out["is_suppressed"] = False
    if "metadata" in data:
        import aws_sdk_support.types.string_list

        out["metadata"] = aws_sdk_support.types.string_list.deserialize_aws_json_1_1(
            data["metadata"]
        )
    else:
        raise DeserializationError("TrustedAdvisorResourceDetail.metadata required")
    return out
