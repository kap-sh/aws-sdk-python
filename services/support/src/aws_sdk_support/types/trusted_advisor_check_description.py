"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.string
    import aws_sdk_support.types.string_list


class TrustedAdvisorCheckDescription(TypedDict):
    id: "aws_sdk_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    name: "aws_sdk_support.types.string.String"
    """<p>The display name for the Trusted Advisor check.</p>"""
    description: "aws_sdk_support.types.string.String"
    """<p>The description of the Trusted Advisor check, which includes the alert criteria and recommended operations (contains HTML markup).</p>"""
    category: "aws_sdk_support.types.string.String"
    """<p>The category of the Trusted Advisor check.</p>"""
    metadata: "aws_sdk_support.types.string_list.StringList"
    """<p>The column headings for the data returned by the Trusted Advisor check. The order of the headings corresponds to the order of the data in the <b>Metadata</b> element of the <a>TrustedAdvisorResourceDetail</a> for the check. <b>Metadata</b> contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckDescription) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["category"] = value["category"]
    import aws_sdk_support.types.string_list

    out["metadata"] = aws_sdk_support.types.string_list.serialize_aws_json_1_1(
        value["metadata"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckDescription:
    out: TrustedAdvisorCheckDescription = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("TrustedAdvisorCheckDescription.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TrustedAdvisorCheckDescription.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckDescription.description required"
        )
    if "category" in data:
        out["category"] = data["category"]
    else:
        raise DeserializationError("TrustedAdvisorCheckDescription.category required")
    if "metadata" in data:
        import aws_sdk_support.types.string_list

        out["metadata"] = aws_sdk_support.types.string_list.deserialize_aws_json_1_1(
            data["metadata"]
        )
    else:
        raise DeserializationError("TrustedAdvisorCheckDescription.metadata required")
    return out
