"""Generated from Smithy shape ``com.amazonaws.synthetics#StartCanaryDryRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.dry_run_config_output


class StartCanaryDryRunResponse(TypedDict, closed=True):
    dry_run_config: NotRequired[
        "capo_synthetics.types.dry_run_config_output.DryRunConfigOutput"
    ]
    """<p>Returns the dry run configurations for a canary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCanaryDryRunResponse) -> dict:
    out: dict = {}
    if "dry_run_config" in value:
        import capo_synthetics.types.dry_run_config_output

        out["DryRunConfig"] = (
            capo_synthetics.types.dry_run_config_output.serialize_json(
                value["dry_run_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCanaryDryRunResponse:
    out: StartCanaryDryRunResponse = {}  # type: ignore[typeddict-item]
    if "DryRunConfig" in data:
        import capo_synthetics.types.dry_run_config_output

        out["dry_run_config"] = (
            capo_synthetics.types.dry_run_config_output.deserialize_json(
                data["DryRunConfig"]
            )
        )
    return out
