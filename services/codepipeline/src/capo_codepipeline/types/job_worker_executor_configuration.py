"""Generated from Smithy shape ``com.amazonaws.codepipeline#JobWorkerExecutorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.polling_account_list
    import capo_codepipeline.types.polling_service_principal_list


class JobWorkerExecutorConfiguration(TypedDict, closed=True):
    polling_accounts: NotRequired[
        "capo_codepipeline.types.polling_account_list.PollingAccountList"
    ]
    """<p>The accounts in which the job worker is configured and might poll for jobs as part of the action execution.</p>"""
    polling_service_principals: NotRequired[
        "capo_codepipeline.types.polling_service_principal_list.PollingServicePrincipalList"
    ]
    """<p>The service Principals in which the job worker is configured and might poll for jobs as part of the action execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobWorkerExecutorConfiguration) -> dict:
    out: dict = {}
    if "polling_accounts" in value:
        import capo_codepipeline.types.polling_account_list

        out["pollingAccounts"] = (
            capo_codepipeline.types.polling_account_list.serialize_aws_json_1_1(
                value["polling_accounts"]
            )
        )
    if "polling_service_principals" in value:
        import capo_codepipeline.types.polling_service_principal_list

        out["pollingServicePrincipals"] = (
            capo_codepipeline.types.polling_service_principal_list.serialize_aws_json_1_1(
                value["polling_service_principals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobWorkerExecutorConfiguration:
    out: JobWorkerExecutorConfiguration = {}  # type: ignore[typeddict-item]
    if "pollingAccounts" in data:
        import capo_codepipeline.types.polling_account_list

        out["polling_accounts"] = (
            capo_codepipeline.types.polling_account_list.deserialize_aws_json_1_1(
                data["pollingAccounts"]
            )
        )
    if "pollingServicePrincipals" in data:
        import capo_codepipeline.types.polling_service_principal_list

        out["polling_service_principals"] = (
            capo_codepipeline.types.polling_service_principal_list.deserialize_aws_json_1_1(
                data["pollingServicePrincipals"]
            )
        )
    return out
