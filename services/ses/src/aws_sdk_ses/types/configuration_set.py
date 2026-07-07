"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_name


class ConfigurationSet(TypedDict, closed=True):
    name: "aws_sdk_ses.types.configuration_set_name.ConfigurationSetName"
    """<p>The name of the configuration set. The name must meet the following requirements:</p> <ul> <li> <p>Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> ConfigurationSet:
    out: ConfigurationSet = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("ConfigurationSet.name required")
    return out
