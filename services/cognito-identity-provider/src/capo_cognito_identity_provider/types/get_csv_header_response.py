"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetCSVHeaderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.list_of_string_types
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetCSVHeaderResponse(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the requested user pool.</p>"""
    csv_header: NotRequired[
        "capo_cognito_identity_provider.types.list_of_string_types.ListOfStringTypes"
    ]
    """<p>A comma-separated list of attributes from your user pool. Save this output to a <code>.csv</code> file and populate it with the attributes of the users that you want to import.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCSVHeaderResponse) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "csv_header" in value:
        import capo_cognito_identity_provider.types.list_of_string_types

        out["CSVHeader"] = (
            capo_cognito_identity_provider.types.list_of_string_types.serialize_aws_json_1_1(
                value["csv_header"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCSVHeaderResponse:
    out: GetCSVHeaderResponse = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "CSVHeader" in data:
        import capo_cognito_identity_provider.types.list_of_string_types

        out["csv_header"] = (
            capo_cognito_identity_provider.types.list_of_string_types.deserialize_aws_json_1_1(
                data["CSVHeader"]
            )
        )
    return out
