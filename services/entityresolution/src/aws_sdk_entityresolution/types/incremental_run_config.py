"""Generated from Smithy shape ``com.amazonaws.entityresolution#IncrementalRunConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.incremental_run_type


class IncrementalRunConfig(TypedDict, closed=True):
    incremental_run_type: NotRequired[
        "aws_sdk_entityresolution.types.incremental_run_type.IncrementalRunType"
    ]
    r"""<p>The type of incremental run. The only valid value is <code>IMMEDIATE</code>. This appears as \"Automatic\" in the console.</p> <important> <p>For workflows where <code>resolutionType</code> is <code>ML_MATCHING</code> or <code>PROVIDER</code>, incremental processing is not supported. </p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncrementalRunConfig) -> dict:
    out: dict = {}
    if "incremental_run_type" in value:
        import aws_sdk_entityresolution.types.incremental_run_type

        out["incrementalRunType"] = (
            aws_sdk_entityresolution.types.incremental_run_type.serialize_json(
                value["incremental_run_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> IncrementalRunConfig:
    out: IncrementalRunConfig = {}  # type: ignore[typeddict-item]
    if "incrementalRunType" in data:
        import aws_sdk_entityresolution.types.incremental_run_type

        out["incremental_run_type"] = (
            aws_sdk_entityresolution.types.incremental_run_type.deserialize_json(
                data["incrementalRunType"]
            )
        )
    return out
