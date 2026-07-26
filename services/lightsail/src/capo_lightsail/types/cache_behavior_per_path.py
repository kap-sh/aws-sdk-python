"""Generated from Smithy shape ``com.amazonaws.lightsail#CacheBehaviorPerPath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.behavior_enum
    import capo_lightsail.types.string


class CacheBehaviorPerPath(TypedDict, closed=True):
    path: NotRequired["capo_lightsail.types.string.string"]
    """<p>The path to a directory or file to cached, or not cache. Use an asterisk symbol to specify wildcard directories (<code>path/to/assets/*</code>), and file types (<code>*.html, *jpg, *js</code>). Directories and file paths are case-sensitive.</p> <p>Examples:</p> <ul> <li> <p>Specify the following to cache all files in the document root of an Apache web server running on a Lightsail instance.</p> <p> <code>var/www/html/</code> </p> </li> <li> <p>Specify the following file to cache only the index page in the document root of an Apache web server.</p> <p> <code>var/www/html/index.html</code> </p> </li> <li> <p>Specify the following to cache only the .html files in the document root of an Apache web server.</p> <p> <code>var/www/html/*.html</code> </p> </li> <li> <p>Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server.</p> <p> <code>var/www/html/images/*.jpg</code> </p> <p> <code>var/www/html/images/*.png</code> </p> <p> <code>var/www/html/images/*.gif</code> </p> <p>Specify the following to cache all files in the images sub-directory of the document root of an Apache web server.</p> <p> <code>var/www/html/images/</code> </p> </li> </ul>"""
    behavior: NotRequired["capo_lightsail.types.behavior_enum.BehaviorEnum"]
    """<p>The cache behavior for the specified path.</p> <p>You can specify one of the following per-path cache behaviors:</p> <ul> <li> <p> <b> <code>cache</code> </b> - This behavior caches the specified path. </p> </li> <li> <p> <b> <code>dont-cache</code> </b> - This behavior doesn't cache the specified path. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheBehaviorPerPath) -> dict:
    out: dict = {}
    if "path" in value:
        out["path"] = value["path"]
    if "behavior" in value:
        import capo_lightsail.types.behavior_enum

        out["behavior"] = capo_lightsail.types.behavior_enum.serialize_aws_json_1_1(
            value["behavior"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheBehaviorPerPath:
    out: CacheBehaviorPerPath = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    if "behavior" in data:
        import capo_lightsail.types.behavior_enum

        out["behavior"] = capo_lightsail.types.behavior_enum.deserialize_aws_json_1_1(
            data["behavior"]
        )
    return out
