"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#CreateHomeRegionControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migrationhub_config.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.dry_run
    import aws_sdk_migrationhub_config.types.home_region
    import aws_sdk_migrationhub_config.types.target


class CreateHomeRegionControlRequest(TypedDict):
    home_region: "aws_sdk_migrationhub_config.types.home_region.HomeRegion"
    """<p>The name of the home region of the calling account.</p>"""
    target: "aws_sdk_migrationhub_config.types.target.Target"
    """<p>The account for which this command sets up a home region control. The <code>Target</code> is always of type <code>ACCOUNT</code>.</p>"""
    dry_run: "aws_sdk_migrationhub_config.types.dry_run.DryRun"
    """<p>Optional Boolean flag to indicate whether any effect should take place. It tests whether the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHomeRegionControlRequest) -> dict:
    out: dict = {}
    out["HomeRegion"] = value["home_region"]
    import aws_sdk_migrationhub_config.types.target

    out["Target"] = aws_sdk_migrationhub_config.types.target.serialize_aws_json_1_1(
        value["target"]
    )
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHomeRegionControlRequest:
    out: CreateHomeRegionControlRequest = {}  # type: ignore[typeddict-item]
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    else:
        raise DeserializationError(
            "CreateHomeRegionControlRequest.home_region required"
        )
    if "Target" in data:
        import aws_sdk_migrationhub_config.types.target

        out["target"] = (
            aws_sdk_migrationhub_config.types.target.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    else:
        raise DeserializationError("CreateHomeRegionControlRequest.target required")
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
