"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateScalingParametersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name
    import aws_sdk_cloudsearch.types.scaling_parameters


class UpdateScalingParametersRequest(TypedDict):
    domain_name: "aws_sdk_cloudsearch.types.domain_name.DomainName"
    scaling_parameters: "aws_sdk_cloudsearch.types.scaling_parameters.ScalingParameters"


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateScalingParametersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.DomainName", str(value["domain_name"])))
    import aws_sdk_cloudsearch.types.scaling_parameters

    aws_sdk_cloudsearch.types.scaling_parameters.serialize_query(
        value["scaling_parameters"], pairs, f"{prefix}.ScalingParameters"
    )


def deserialize_query(el: Element) -> UpdateScalingParametersRequest:
    out: UpdateScalingParametersRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        raise DeserializationError(
            "UpdateScalingParametersRequest.domain_name required"
        )
    child_scaling_parameters = el.find("ScalingParameters")
    if child_scaling_parameters is not None:
        import aws_sdk_cloudsearch.types.scaling_parameters

        out["scaling_parameters"] = (
            aws_sdk_cloudsearch.types.scaling_parameters.deserialize_query(
                child_scaling_parameters
            )
        )
    else:
        raise DeserializationError(
            "UpdateScalingParametersRequest.scaling_parameters required"
        )
    return out
