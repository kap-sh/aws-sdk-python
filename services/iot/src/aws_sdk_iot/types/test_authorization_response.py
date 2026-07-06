"""Generated from Smithy shape ``com.amazonaws.iot#TestAuthorizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.auth_results


class TestAuthorizationResponse(TypedDict, closed=True):
    auth_results: NotRequired["aws_sdk_iot.types.auth_results.AuthResults"]
    """<p>The authentication results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestAuthorizationResponse) -> dict:
    out: dict = {}
    if "auth_results" in value:
        import aws_sdk_iot.types.auth_results

        out["authResults"] = aws_sdk_iot.types.auth_results.serialize_json(
            value["auth_results"]
        )
    return out


def deserialize_json(data: dict) -> TestAuthorizationResponse:
    out: TestAuthorizationResponse = {}  # type: ignore[typeddict-item]
    if "authResults" in data:
        import aws_sdk_iot.types.auth_results

        out["auth_results"] = aws_sdk_iot.types.auth_results.deserialize_json(
            data["authResults"]
        )
    return out
