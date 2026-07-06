"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationGrantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.grant


class GetApplicationGrantResponse(TypedDict, closed=True):
    grant: "aws_sdk_sso_admin.types.grant.Grant"
    """<p>A structure that describes the requested grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationGrantResponse) -> dict:
    out: dict = {}
    import aws_sdk_sso_admin.types.grant

    out["Grant"] = aws_sdk_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationGrantResponse:
    out: GetApplicationGrantResponse = {}  # type: ignore[typeddict-item]
    if "Grant" in data:
        import aws_sdk_sso_admin.types.grant

        out["grant"] = aws_sdk_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        raise DeserializationError("GetApplicationGrantResponse.grant required")
    return out
