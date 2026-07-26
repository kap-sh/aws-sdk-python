"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetTestGridSessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.test_grid_session


class GetTestGridSessionResult(TypedDict, closed=True):
    test_grid_session: NotRequired[
        "capo_device_farm.types.test_grid_session.TestGridSession"
    ]
    """<p>The <a>TestGridSession</a> that was requested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTestGridSessionResult) -> dict:
    out: dict = {}
    if "test_grid_session" in value:
        import capo_device_farm.types.test_grid_session

        out["testGridSession"] = (
            capo_device_farm.types.test_grid_session.serialize_aws_json_1_1(
                value["test_grid_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTestGridSessionResult:
    out: GetTestGridSessionResult = {}  # type: ignore[typeddict-item]
    if "testGridSession" in data:
        import capo_device_farm.types.test_grid_session

        out["test_grid_session"] = (
            capo_device_farm.types.test_grid_session.deserialize_aws_json_1_1(
                data["testGridSession"]
            )
        )
    return out
