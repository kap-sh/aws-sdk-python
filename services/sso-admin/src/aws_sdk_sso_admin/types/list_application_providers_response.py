"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.application_provider_list
    import aws_sdk_sso_admin.types.token


class ListApplicationProvidersResponse(TypedDict, closed=True):
    application_providers: NotRequired[
        "aws_sdk_sso_admin.types.application_provider_list.ApplicationProviderList"
    ]
    """<p>An array list of structures that describe application providers.</p>"""
    next_token: NotRequired["aws_sdk_sso_admin.types.token.Token"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationProvidersResponse) -> dict:
    out: dict = {}
    if "application_providers" in value:
        import aws_sdk_sso_admin.types.application_provider_list

        out["ApplicationProviders"] = (
            aws_sdk_sso_admin.types.application_provider_list.serialize_aws_json_1_1(
                value["application_providers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationProvidersResponse:
    out: ListApplicationProvidersResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationProviders" in data:
        import aws_sdk_sso_admin.types.application_provider_list

        out["application_providers"] = (
            aws_sdk_sso_admin.types.application_provider_list.deserialize_aws_json_1_1(
                data["ApplicationProviders"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
