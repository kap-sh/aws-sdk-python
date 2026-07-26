"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ScalingParametersStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.option_status
    import capo_cloudsearch.types.scaling_parameters


class ScalingParametersStatus(TypedDict, closed=True):
    options: "capo_cloudsearch.types.scaling_parameters.ScalingParameters"
    status: "capo_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingParametersStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudsearch.types.scaling_parameters

    capo_cloudsearch.types.scaling_parameters.serialize_query(
        value["options"], pairs, f"{prefix}.Options"
    )
    import capo_cloudsearch.types.option_status

    capo_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> ScalingParametersStatus:
    out: ScalingParametersStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import capo_cloudsearch.types.scaling_parameters

        out["options"] = capo_cloudsearch.types.scaling_parameters.deserialize_query(
            child_options
        )
    else:
        raise DeserializationError("ScalingParametersStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudsearch.types.option_status

        out["status"] = capo_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("ScalingParametersStatus.status required")
    return out
