"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ValidatePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.token
    import aws_sdk_accessanalyzer.types.validate_policy_finding_list


class ValidatePolicyResponse(TypedDict, closed=True):
    findings: "aws_sdk_accessanalyzer.types.validate_policy_finding_list.ValidatePolicyFindingList"
    """<p>The list of findings in a policy returned by IAM Access Analyzer based on its suite of policy checks.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidatePolicyResponse) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.validate_policy_finding_list

    out["findings"] = (
        aws_sdk_accessanalyzer.types.validate_policy_finding_list.serialize_json(
            value["findings"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ValidatePolicyResponse:
    out: ValidatePolicyResponse = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_accessanalyzer.types.validate_policy_finding_list

        out["findings"] = (
            aws_sdk_accessanalyzer.types.validate_policy_finding_list.deserialize_json(
                data["findings"]
            )
        )
    else:
        raise DeserializationError("ValidatePolicyResponse.findings required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
