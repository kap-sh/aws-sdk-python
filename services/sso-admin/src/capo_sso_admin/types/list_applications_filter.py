"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ListApplicationsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_id
    import capo_sso_admin.types.application_provider_arn


class ListApplicationsFilter(TypedDict, closed=True):
    application_account: NotRequired["capo_sso_admin.types.account_id.AccountId"]
    """<p>An Amazon Web Services account ID number that filters the results in the response.</p>"""
    application_provider: NotRequired[
        "capo_sso_admin.types.application_provider_arn.ApplicationProviderArn"
    ]
    """<p>The ARN of an application provider that can filter the results in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsFilter) -> dict:
    out: dict = {}
    if "application_account" in value:
        out["ApplicationAccount"] = value["application_account"]
    if "application_provider" in value:
        out["ApplicationProvider"] = value["application_provider"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsFilter:
    out: ListApplicationsFilter = {}  # type: ignore[typeddict-item]
    if "ApplicationAccount" in data:
        out["application_account"] = data["ApplicationAccount"]
    if "ApplicationProvider" in data:
        out["application_provider"] = data["ApplicationProvider"]
    return out
