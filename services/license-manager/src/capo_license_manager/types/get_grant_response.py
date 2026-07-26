"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetGrantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.grant


class GetGrantResponse(TypedDict, closed=True):
    grant: NotRequired["capo_license_manager.types.grant.Grant"]
    """<p>Grant details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGrantResponse) -> dict:
    out: dict = {}
    if "grant" in value:
        import capo_license_manager.types.grant

        out["Grant"] = capo_license_manager.types.grant.serialize_aws_json_1_1(
            value["grant"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGrantResponse:
    out: GetGrantResponse = {}  # type: ignore[typeddict-item]
    if "Grant" in data:
        import capo_license_manager.types.grant

        out["grant"] = capo_license_manager.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    return out
