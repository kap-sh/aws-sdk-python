"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#PutApplicationPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement


class PutApplicationPolicyResponse(TypedDict, closed=True):
    statements: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.__listOfApplicationPolicyStatement"
    ]
    """<p>An array of policy statements applied to the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutApplicationPolicyResponse) -> dict:
    out: dict = {}
    if "statements" in value:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement

        out["statements"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.serialize_json(
                value["statements"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutApplicationPolicyResponse:
    out: PutApplicationPolicyResponse = {}  # type: ignore[typeddict-item]
    if "statements" in data:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement

        out["statements"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.deserialize_json(
                data["statements"]
            )
        )
    return out
