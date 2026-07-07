"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_account_id
    import aws_sdk_datazone.types.aws_region
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.environment_profile_id
    import aws_sdk_datazone.types.environment_profile_name


class UpdateEnvironmentProfileInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which an environment profile is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.environment_profile_id.EnvironmentProfileId"
    """<p>The identifier of the environment profile that is to be updated.</p>"""
    name: NotRequired[
        "aws_sdk_datazone.types.environment_profile_name.EnvironmentProfileName"
    ]
    """<p>The name to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>"""
    aws_account_id: NotRequired["aws_sdk_datazone.types.aws_account_id.AwsAccountId"]
    """<p>The Amazon Web Services account in which a specified environment profile is to be udpated.</p>"""
    aws_account_region: NotRequired["aws_sdk_datazone.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region in which a specified environment profile is to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentProfileInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "aws_account_region" in value:
        out["awsAccountRegion"] = value["aws_account_region"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentProfileInput:
    out: UpdateEnvironmentProfileInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "awsAccountRegion" in data:
        out["aws_account_region"] = data["awsAccountRegion"]
    return out
