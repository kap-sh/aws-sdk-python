"""Generated from Smithy shape ``com.amazonaws.athena#ResultReuseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.result_reuse_by_age_configuration


class ResultReuseConfiguration(TypedDict, closed=True):
    result_reuse_by_age_configuration: NotRequired[
        "aws_sdk_athena.types.result_reuse_by_age_configuration.ResultReuseByAgeConfiguration"
    ]
    """<p>Specifies whether previous query results are reused, and if so, their maximum age.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultReuseConfiguration) -> dict:
    out: dict = {}
    if "result_reuse_by_age_configuration" in value:
        import aws_sdk_athena.types.result_reuse_by_age_configuration

        out["ResultReuseByAgeConfiguration"] = (
            aws_sdk_athena.types.result_reuse_by_age_configuration.serialize_aws_json_1_1(
                value["result_reuse_by_age_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultReuseConfiguration:
    out: ResultReuseConfiguration = {}  # type: ignore[typeddict-item]
    if "ResultReuseByAgeConfiguration" in data:
        import aws_sdk_athena.types.result_reuse_by_age_configuration

        out["result_reuse_by_age_configuration"] = (
            aws_sdk_athena.types.result_reuse_by_age_configuration.deserialize_aws_json_1_1(
                data["ResultReuseByAgeConfiguration"]
            )
        )
    return out
