"""Generated from Smithy shape ``com.amazonaws.rds#DBMajorEngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.supported_engine_lifecycle_list


class DBMajorEngineVersion(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the database engine.</p>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>The major version number of the database engine.</p>"""
    supported_engine_lifecycles: NotRequired[
        "capo_rds.types.supported_engine_lifecycle_list.SupportedEngineLifecycleList"
    ]
    """<p>A list of the lifecycles supported by this engine for the <code>DescribeDBMajorEngineVersions</code> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBMajorEngineVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "supported_engine_lifecycles" in value:
        import capo_rds.types.supported_engine_lifecycle_list

        capo_rds.types.supported_engine_lifecycle_list.serialize_query(
            value["supported_engine_lifecycles"],
            pairs,
            f"{prefix}.SupportedEngineLifecycles",
        )


def deserialize_query(el: Element) -> DBMajorEngineVersion:
    out: DBMajorEngineVersion = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_supported_engine_lifecycles = el.find("SupportedEngineLifecycles")
    if child_supported_engine_lifecycles is not None:
        import capo_rds.types.supported_engine_lifecycle_list

        out["supported_engine_lifecycles"] = (
            capo_rds.types.supported_engine_lifecycle_list.deserialize_query(
                child_supported_engine_lifecycles
            )
        )
    return out
