"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceCollection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_names


class ServiceCollection(TypedDict, closed=True):
    service_names: NotRequired["aws_sdk_devops_guru.types.service_names.ServiceNames"]
    """<p>An array of strings that each specifies the name of an Amazon Web Services service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceCollection) -> dict:
    out: dict = {}
    if "service_names" in value:
        import aws_sdk_devops_guru.types.service_names

        out["ServiceNames"] = aws_sdk_devops_guru.types.service_names.serialize_json(
            value["service_names"]
        )
    return out


def deserialize_json(data: dict) -> ServiceCollection:
    out: ServiceCollection = {}  # type: ignore[typeddict-item]
    if "ServiceNames" in data:
        import aws_sdk_devops_guru.types.service_names

        out["service_names"] = aws_sdk_devops_guru.types.service_names.deserialize_json(
            data["ServiceNames"]
        )
    return out
