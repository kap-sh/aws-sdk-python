"""Generated from Smithy shape ``com.amazonaws.ses#CreateConfigurationSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set


class CreateConfigurationSetRequest(TypedDict):
    configuration_set: "aws_sdk_ses.types.configuration_set.ConfigurationSet"
    """<p>A data structure that contains the name of the configuration set.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateConfigurationSetRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.configuration_set

    aws_sdk_ses.types.configuration_set.serialize_query(
        value["configuration_set"], pairs, f"{prefix}.ConfigurationSet"
    )


def deserialize_query(el: Element) -> CreateConfigurationSetRequest:
    out: CreateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    child_configuration_set = el.find("ConfigurationSet")
    if child_configuration_set is not None:
        import aws_sdk_ses.types.configuration_set

        out["configuration_set"] = (
            aws_sdk_ses.types.configuration_set.deserialize_query(
                child_configuration_set
            )
        )
    else:
        raise DeserializationError(
            "CreateConfigurationSetRequest.configuration_set required"
        )
    return out
