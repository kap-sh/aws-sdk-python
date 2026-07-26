"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryScanningConfigurationFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.repository_name
    import capo_ecr.types.scanning_configuration_failure_code
    import capo_ecr.types.scanning_configuration_failure_reason


class RepositoryScanningConfigurationFailure(TypedDict, closed=True):
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    failure_code: NotRequired[
        "capo_ecr.types.scanning_configuration_failure_code.ScanningConfigurationFailureCode"
    ]
    """<p>The failure code.</p>"""
    failure_reason: NotRequired[
        "capo_ecr.types.scanning_configuration_failure_reason.ScanningConfigurationFailureReason"
    ]
    """<p>The reason for the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryScanningConfigurationFailure) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "failure_code" in value:
        import capo_ecr.types.scanning_configuration_failure_code

        out["failureCode"] = (
            capo_ecr.types.scanning_configuration_failure_code.serialize_aws_json_1_1(
                value["failure_code"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryScanningConfigurationFailure:
    out: RepositoryScanningConfigurationFailure = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "failureCode" in data:
        import capo_ecr.types.scanning_configuration_failure_code

        out["failure_code"] = (
            capo_ecr.types.scanning_configuration_failure_code.deserialize_aws_json_1_1(
                data["failureCode"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
