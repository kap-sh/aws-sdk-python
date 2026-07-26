"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteServiceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service


class DeleteServiceResponse(TypedDict, closed=True):
    service: NotRequired["capo_ecs.types.service.Service"]
    """<p>The full description of the deleted service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServiceResponse) -> dict:
    out: dict = {}
    if "service" in value:
        import capo_ecs.types.service

        out["service"] = capo_ecs.types.service.serialize_aws_json_1_1(value["service"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServiceResponse:
    out: DeleteServiceResponse = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import capo_ecs.types.service

        out["service"] = capo_ecs.types.service.deserialize_aws_json_1_1(
            data["service"]
        )
    return out
