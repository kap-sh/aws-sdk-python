"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.failures
    import capo_ecs.types.services


class DescribeServicesResponse(TypedDict, closed=True):
    services: NotRequired["capo_ecs.types.services.Services"]
    """<p>The list of services described.</p>"""
    failures: NotRequired["capo_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import capo_ecs.types.services

        out["services"] = capo_ecs.types.services.serialize_aws_json_1_1(
            value["services"]
        )
    if "failures" in value:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesResponse:
    out: DescribeServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("services") is not None:
        import capo_ecs.types.services

        out["services"] = capo_ecs.types.services.deserialize_aws_json_1_1(
            data["services"]
        )
    if data.get("failures") is not None:
        import capo_ecs.types.failures

        out["failures"] = capo_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
