"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#PutApplicationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement
    import aws_sdk_serverlessapplicationrepository.types.__string


class PutApplicationPolicyRequest(TypedDict):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    statements: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.__listOfApplicationPolicyStatement"
    ]
    """<p>An array of policy statements applied to the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutApplicationPolicyRequest) -> dict:
    out: dict = {}
    if "statements" in value:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement

        out["statements"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.serialize_json(
                value["statements"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutApplicationPolicyRequest:
    out: PutApplicationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "statements" in data:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement

        out["statements"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_policy_statement.deserialize_json(
                data["statements"]
            )
        )
    return out
