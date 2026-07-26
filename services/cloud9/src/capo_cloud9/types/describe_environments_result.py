"""Generated from Smithy shape ``com.amazonaws.cloud9#DescribeEnvironmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloud9.types.environment_list


class DescribeEnvironmentsResult(TypedDict, closed=True):
    environments: NotRequired["capo_cloud9.types.environment_list.EnvironmentList"]
    """<p>Information about the environments that are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEnvironmentsResult) -> dict:
    out: dict = {}
    if "environments" in value:
        import capo_cloud9.types.environment_list

        out["environments"] = capo_cloud9.types.environment_list.serialize_aws_json_1_1(
            value["environments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEnvironmentsResult:
    out: DescribeEnvironmentsResult = {}  # type: ignore[typeddict-item]
    if "environments" in data:
        import capo_cloud9.types.environment_list

        out["environments"] = (
            capo_cloud9.types.environment_list.deserialize_aws_json_1_1(
                data["environments"]
            )
        )
    return out
