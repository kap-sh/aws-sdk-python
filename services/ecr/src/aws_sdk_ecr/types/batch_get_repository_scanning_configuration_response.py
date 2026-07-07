"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetRepositoryScanningConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.repository_scanning_configuration_failure_list
    import aws_sdk_ecr.types.repository_scanning_configuration_list


class BatchGetRepositoryScanningConfigurationResponse(TypedDict, closed=True):
    scanning_configurations: NotRequired[
        "aws_sdk_ecr.types.repository_scanning_configuration_list.RepositoryScanningConfigurationList"
    ]
    """<p>The scanning configuration for the requested repositories.</p>"""
    failures: NotRequired[
        "aws_sdk_ecr.types.repository_scanning_configuration_failure_list.RepositoryScanningConfigurationFailureList"
    ]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchGetRepositoryScanningConfigurationResponse,
) -> dict:
    out: dict = {}
    if "scanning_configurations" in value:
        import aws_sdk_ecr.types.repository_scanning_configuration_list

        out["scanningConfigurations"] = (
            aws_sdk_ecr.types.repository_scanning_configuration_list.serialize_aws_json_1_1(
                value["scanning_configurations"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecr.types.repository_scanning_configuration_failure_list

        out["failures"] = (
            aws_sdk_ecr.types.repository_scanning_configuration_failure_list.serialize_aws_json_1_1(
                value["failures"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchGetRepositoryScanningConfigurationResponse:
    out: BatchGetRepositoryScanningConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanningConfigurations" in data:
        import aws_sdk_ecr.types.repository_scanning_configuration_list

        out["scanning_configurations"] = (
            aws_sdk_ecr.types.repository_scanning_configuration_list.deserialize_aws_json_1_1(
                data["scanningConfigurations"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecr.types.repository_scanning_configuration_failure_list

        out["failures"] = (
            aws_sdk_ecr.types.repository_scanning_configuration_failure_list.deserialize_aws_json_1_1(
                data["failures"]
            )
        )
    return out
