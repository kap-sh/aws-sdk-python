"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3ExpressDirectoryAccessPointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_point_policy
    import capo_accessanalyzer.types.network_origin_configuration


class S3ExpressDirectoryAccessPointConfiguration(TypedDict, closed=True):
    access_point_policy: NotRequired[
        "capo_accessanalyzer.types.access_point_policy.AccessPointPolicy"
    ]
    """<p>The proposed access point policy for an Amazon S3 directory bucket access point.</p>"""
    network_origin: NotRequired[
        "capo_accessanalyzer.types.network_origin_configuration.NetworkOriginConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: S3ExpressDirectoryAccessPointConfiguration) -> dict:
    out: dict = {}
    if "access_point_policy" in value:
        out["accessPointPolicy"] = value["access_point_policy"]
    if "network_origin" in value:
        import capo_accessanalyzer.types.network_origin_configuration

        out["networkOrigin"] = (
            capo_accessanalyzer.types.network_origin_configuration.serialize_json(
                value["network_origin"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ExpressDirectoryAccessPointConfiguration:
    out: S3ExpressDirectoryAccessPointConfiguration = {}  # type: ignore[typeddict-item]
    if "accessPointPolicy" in data:
        out["access_point_policy"] = data["accessPointPolicy"]
    if "networkOrigin" in data:
        import capo_accessanalyzer.types.network_origin_configuration

        out["network_origin"] = (
            capo_accessanalyzer.types.network_origin_configuration.deserialize_json(
                data["networkOrigin"]
            )
        )
    return out
